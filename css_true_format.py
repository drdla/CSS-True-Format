import sublime, sublime_plugin, sys, os, inspect

if sys.version_info < (3, 0):
	# ST2, Python 2.6
	from libs.cssformatter import format_code
else:
	# ST3, Python 3.3
	from .libs.cssformatter import format_code

    SETTINGS_FILE = 'CSSTrueFormat.sublime-settings'

def has_css_syntax(view):
    file_name = view.file_name()
    syntaxPath = view.settings().get('syntax')
    syntax = ''
    extension = ''

    css_family = ['css', 'sass', 'scss', 'less']

    if (file_name != None): # file exists, pull syntax type from extension
        extension = os.path.splitext(file_name)[1][1:]
    if (syntaxPath != None):
        syntax = os.path.splitext(syntaxPath)[0].split('/')[-1].lower()

    return extension in css_family or syntax in css_family


class PreSaveFormatListner(sublime_plugin.EventListener):
    """Event listener to run CSS True Format during the presave event"""
    def on_pre_save(self, view):
        settings = sublime.load_settings(SETTINGS_FILE)
        should_format = settings.get('format_on_save') and has_css_syntax(view)
        if has_css_syntax(view):
            view.run_command('css_true_format')


class CssTrueFormatCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view

		if view.is_loading():
			sublime.status_message('Waiting to be loaded.')
			return False

		selection = view.sel()[0]
		if len(selection) > 0:
			self.format_selection(edit)
		else:
			self.format_whole_file(edit)

	def format_selection(self, edit):
		view = self.view
		regions = []

		for sel in view.sel():
			region = sublime.Region(
				view.line(min(sel.a, sel.b)).a,  # line start of first line
				view.line(max(sel.a, sel.b)).b   # line end of last line
			)
			code = view.substr(region)
			code = format_code(code)
			view.replace(edit, region, code)

	def format_whole_file(self, edit):
		view = self.view
		region = sublime.Region(0, view.size())
		code = view.substr(region)
		code = format_code(code)
		view.replace(edit, region, code)

	def is_visible(self):
		return has_css_syntax(self.view)

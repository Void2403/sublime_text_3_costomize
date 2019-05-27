import webbrowser

import sublime_plugin


class OpenInBrowserCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if self.view.file_name():
            webbrowser.open_new_tab("file://" + self.view.file_name())

    def is_visible(self):
        return self.view.file_name() is not None and (
            self.view.file_name()[-5:] == ".html" or
            self.view.file_name()[-5:] == ".HTML" or
            self.view.file_name()[-4:] == ".htm" or
            self.view.file_name()[-4:] == ".HTM")

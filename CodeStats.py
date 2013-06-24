#http://net.tutsplus.com/tutorials/python-tutorials/how-to-create-a-sublime-text-2-plugin/
import sublime, sublime_plugin
count = 0
class CodeStats(sublime_plugin.EventListener):
	clicks = 0
	clicksTrigger = 1
	count = 0

	def on_modified(self, view):
		self.clicks += 1
		self.count += 1
		if self.clicks >= self.clicksTrigger:
			print "code written", self.count
			self.clicks = 0
			##showStats()


##
##def showStats()
##	print(count)
##	return
# -*- coding: utf-8 -*-
try:
	import wxversion
	try:
		wxversion.select('2.8')
	except:
		pass
except:
	pass
import wx as DamnWx
import wx.animate
from wx.lib.mixins.listctrl import ListCtrlAutoWidthMixin
import wx.lib.stattext
wx = DamnWx
wx.ListCtrlAutoWidthMixin = ListCtrlAutoWidthMixin
del DamnWx, ListCtrlAutoWidthMixin
try:
	del wxversion
except:
	pass

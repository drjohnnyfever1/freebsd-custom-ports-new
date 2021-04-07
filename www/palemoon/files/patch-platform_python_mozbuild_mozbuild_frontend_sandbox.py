--- ./platform/python/mozbuild/mozbuild/frontend/sandbox.py~	2020-10-24 10:42:23.000000000 +0000
+++ ./platform/python/mozbuild/mozbuild/frontend/sandbox.py	2020-11-09 12:38:55.634959000 +0000
@@ -115,7 +115,10 @@
     def __init__(self, context, builtins=None, finder=default_finder):
         """Initialize a Sandbox ready for execution.
         """
-        self._builtins = builtins or self.BUILTINS
+        self._builtins = ReadOnlyDict(
+            (builtins or self.BUILTINS).viewitems() |
+            {b: __builtins__[b] for b in ('__build_class__',)
+             if b in __builtins__}.viewitems())
         dict.__setitem__(self, '__builtins__', self._builtins)
 
         assert isinstance(self._builtins, ReadOnlyDict)

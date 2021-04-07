--- ./platform/python/mozbuild/mozbuild/configure/__init__.py~	2020-10-24 10:42:23.000000000 +0000
+++ ./platform/python/mozbuild/mozbuild/configure/__init__.py	2020-11-09 12:31:00.109014000 +0000
@@ -192,8 +192,9 @@
         b: __builtins__[b]
         for b in ('None', 'False', 'True', 'int', 'bool', 'any', 'all', 'len',
                   'list', 'tuple', 'set', 'dict', 'isinstance', 'getattr',
-                  'hasattr', 'enumerate', 'range', 'zip')
-    }, __import__=forbidden_import, str=unicode)
+                  'hasattr', 'enumerate', 'range', 'zip', '__build_class__')
+        if b in __builtins__},
+    __import__=forbidden_import, str=unicode)
 
     # Expose a limited set of functions from os.path
     OS = ReadOnlyNamespace(path=ReadOnlyNamespace(**{

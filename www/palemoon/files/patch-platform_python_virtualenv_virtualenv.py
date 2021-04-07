--- ./platform/python/virtualenv/virtualenv.py	2020-10-24 10:42:23.000000000 +0000
+++ ./platform/python/virtualenv/virtualenv.py	2020-11-09 14:29:09.153232000 +0000
@@ -49,7 +49,7 @@
 except NameError:
     basestring = str
 
-py_version = 'python%s.%s' % (sys.version_info[0], sys.version_info[1])
+py_version = 'tauthon%s.%s' % (sys.version_info[0], sys.version_info[1])
 
 is_jython = sys.platform.startswith('java')
 is_pypy = hasattr(sys, 'pypy_version_info')
@@ -131,6 +131,8 @@
         REQUIRED_MODULES.extend(['warnings', 'linecache', '_abcoll', 'abc'])
     if minver >= 7:
         REQUIRED_MODULES.extend(['_weakrefset'])
+    if minver >= 8:
+        REQUIRED_MODULES.extend(['_oserror'])
     if is_msys2:
         REQUIRED_MODULES.extend(['functools'])
 elif majver == 3:

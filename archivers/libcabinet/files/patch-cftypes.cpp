--- cftypes.cpp.orig	Sat Oct 23 23:13:29 1999
+++ cftypes.cpp	Sun Aug 31 06:07:25 2003
@@ -10,7 +10,15 @@
 #ifndef __CFTYPES_CPP__
 #define __CFTYPES_CPP__
 
-#include <values.h>
+#ifndef MAXSHORT
+#define BITSPERBYTE 8
+#define BITS(type)  (BITSPERBYTE * (int)sizeof(type))
+#define SHORTBITS   BITS(int16_t)
+#define MINSHORT    ((int16_t)(1 << (SHORTBITS - 1)))
+#define MAXSHORT    ((int16_t)~MINSHORT)
+#endif
+
+#include <limits.h>
 #include <fstream.h>
 #include "zlib.h"
 #include "cftypes.h"
@@ -138,15 +146,20 @@
 
 int io_read(istream& in, byte* buf, word len)
 {
-	while(len > MAXINT)
+	// replaced MAXINT with MAXSHORT, since len is of type
+	// word == unsigned short int
+	//
+	// TODO: please review this, since IMO the while-loop is
+	// never entered
+	while (len > MAXSHORT)
 	{
-		if(in.read(buf, MAXINT).bad())
+		if(in.read((char*)buf, MAXSHORT).bad())
 			return (in.fail()) ? READ_ERROR : UNEXPECTED_EOF;
-		len -= (word) MAXINT;
-		buf += (word) MAXINT;
+		len -= (word) MAXSHORT;
+		buf += (word) MAXSHORT;
 	}
 
-	return (in.read(buf, (int) len).bad())
+	return (in.read((char*)buf, (int) len).bad())
 		? (in.fail()) ? READ_ERROR : UNEXPECTED_EOF : OK;
 }
 
@@ -154,14 +167,19 @@
 
 int io_write(ostream& out, const byte* buf, word len)
 {
-	while(len > MAXINT)
+	// replaced MAXINT with MAXSHORT, since len is of type
+	// word == unsigned short int
+	//
+	// TODO: please review this, since IMO the while-loop is
+	// never entered
+	while(len > MAXSHORT)
 	{
-		if(out.write(buf, MAXINT).fail()) return WRITE_ERROR;
-		len -= (word) MAXINT;
-		buf += (word) MAXINT;
+		if(out.write((char*)buf, MAXSHORT).fail()) return WRITE_ERROR;
+		len -= (word) MAXSHORT;
+		buf += (word) MAXSHORT;
 	}
 
-	return (out.write(buf, (int) len).fail()) ? WRITE_ERROR : OK;
+	return (out.write((char*)buf, (int) len).fail()) ? WRITE_ERROR : OK;
 }
 
 //*****************************************************************************/

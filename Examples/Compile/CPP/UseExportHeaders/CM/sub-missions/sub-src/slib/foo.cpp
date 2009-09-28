#include "foo.h"
#include "ExportHello.h"

char BUF[1000];

char * foo()
{
	char * buf = BUF;
	char * mess = "This is goal of sub-proxy customer.\n";
	int p = 0;
	for ( int i = 0; mess[i]; buf[p++] = mess[i++] );
	ExportHello exportHello;
	char * exhm = exportHello.Get();
	for ( int i = 0; exhm[i]; buf[p++] = exhm[i++] );
	return buf;
}

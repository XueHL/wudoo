#include "Hello.h"

char * HelloDebug()
{
	int sum = 0;
	for ( int i = 0; i < 100; i++ )
	{
		for ( int j = 0; j < 100; j++ )
		{
			sum += i * j;
			if ( sum % 123 == 32 )
			{
				sum &= ( 1 << 10 ) - 1;
			}
		}
	}
	return "Hello debug!";
}

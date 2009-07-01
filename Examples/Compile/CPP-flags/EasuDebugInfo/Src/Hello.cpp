#include "Hello.h"

char * HelloDebug()
{
	int sum = 0;
	for ( int i = 0; i < 10; i++ )
	{
		for ( int j = 0; j < 10; j++ )
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

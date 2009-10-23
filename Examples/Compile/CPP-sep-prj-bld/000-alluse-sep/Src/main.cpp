#include<iostream.h>

#include<boost/shared_ptr.hpp>

#include"SufString.h"

typedef boost::shared_ptr< SufString > SufStringPtr;

int main( int count, char * * agrs )
{
	SufStringPtr sstr( new SufString( "Hello" ) );

	std::cout << sstr->Get() << "\n";
}

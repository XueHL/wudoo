#include <boost/shared_ptr.hpp>

#include <vector>

#include "sharedptrtest.h"

int ShPtrTst::destroyed = 0;
int ShPtrTst::created = 0;

ShPtrTst::ShPtrTst()
{
	created++;
}

ShPtrTst::ShPtrTst( const ShPtrTst & spt )
{
	created++;
}

ShPtrTst::~ShPtrTst()
{
	destroyed++;
}

int ShPtrTst::Created()
{
	return created;
}

int ShPtrTst::Destroyed()
{
	return destroyed;
}

void RunShPtrTest()
{
	{
		std::vector< ShPtrTst > spvec( 10 );
		ShPtrTst elem3 = spvec[3];
	}

	{
		std::vector< boost::shared_ptr< ShPtrTst > > spvec( 10 );
		for ( int i = 0; i < spvec.size(); i++ )
		{
			spvec[i] = new ShPtrTst();
		}
		ShPtrTst elem3 = spvec[3].get();
	}
}

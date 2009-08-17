class ShPtrTst
{
public:
	ShPtrTst();
	ShPtrTst( const ShPtrTst & spt );
	~ShPtrTst();
public:
	static int Created();
	static int Destroyed();
private:
	static int created;
	static int destroyed;
};

void RunShPtrTest();

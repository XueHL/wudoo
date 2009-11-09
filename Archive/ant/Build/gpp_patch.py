import os

p = os.path.join("cpptasks-1.0b5", "src", "main", "java", "net", "sf", "antcontrib", "cpptasks", "gcc", "GccCCompiler.java")
b = open(p).read()
assert(b.find(
"""\
    public Linker getLinker(LinkType linkType) {
        return GccLinker.getInstance().getLinker(linkType);
    }\
"""
) > -1)

b = b.replace(
"""\
    public Linker getLinker(LinkType linkType) {
        return GccLinker.getInstance().getLinker(linkType);
    }\
""",
"""\
    public Linker getLinker(LinkType linkType) {
    	if (getCommand().equals("g++")) return GppLinker.getInstance().getLinker(linkType);
        return GccLinker.getInstance().getLinker(linkType);
    }\
"""
)
f = open(p, "w")
f.write(b)
f.close()


### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 


p = os.path.join("cpptasks-1.0b5", "src", "main", "java", "net", "sf", "antcontrib", "cpptasks", "gcc", "GppLinker.java")
b = open(p).read()
assert(b.find('= new GppLinker("gcc",') > -1)
b = b.replace('= new GppLinker("gcc",', '= new GppLinker("g++",')
f = open(p, "w")
f.write(b)
f.close()
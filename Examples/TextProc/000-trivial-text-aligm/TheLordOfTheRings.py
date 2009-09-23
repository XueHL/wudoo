from wudoo.textproc.Front import *

tproc = getTextProc("the-lord-of-the-lings--wikipedia-article", __file__)

tproc.setBookName("Wikipedia about TLotR")

tproc.addHeader(level = 0, headerText = "The Lord of the Rings")

tproc.newParagraph()

tproc.write(
"""
The Lord of the Rings is an epic high fantasy novel written by philologist and Oxford University 
professor J. R. R. Tolkien. The story began as a sequel to Tolkien's earlier, less complex children's 
fantasy novel The Hobbit (1937), but eventually developed into a much larger work. It was written 
in stages between 1937 and 1949, much of it during World War II.[1] Although generally known 
"""
)
tproc.write(
"""
to readers as a trilogy, the work was initially intended by Tolkien to be one volume of 
a two-volume set along with The Silmarillion; however, the publisher decided to omit the second 
volume and instead published The Lord of the Rings in 1954-55 as three books rather than one, 
mr economic reasons.[2] It has since been reprinted numerous times and translated into many 
languages, becoming one of the most popular and influential works in 20th-century literature.
"""
)

tproc.newParagraph()

tproc.write(
"""
The title of the book refers to the story's main antagonist, the Dark Lord Sauron, who had in an 
earlier age created the One Ring to rule the other Rings of Power, as the ultimate weapon in his 
campaign to conquer and rule all of Middle-earth. From quiet beginnings in the Shire, a hobbit 
land not unlike the English countryside, the story ranges across Middle-earth following the course 
of the War of the Ring through the eyes of its characters, most notably the hobbits, Frodo Baggins, 
Samwise Gamgee (Sam), Meriadoc Brandybuck (Merry) and Peregrin Took (Pippin).
"""
)

tproc.newParagraph()

tproc.write(
"""
Along with Tolkien's other works, The Lord of the Rings has been subjected to extensive analysis of 
its themes and origins. Although a major work in itself, the story was only the last movement of a 
larger work Tolkien had worked on since 1917, in a process he described as mythopoeia.[3] Influences 
on this earlier work, and on the story of The Lord of the Rings, include philology, mythology, religion 
and the author's distaste for the effects of industrialization, as well as earlier fantasy works and 
Tolkien's experiences in World War I.[4] The Lord of the Rings in its turn is considered to have had 
a great effect on modern fantasy; the impact of Tolkien's works is such that the use of the words 
"Tolkienian" and "Tolkienesque" has been recorded in the Oxford English Dictionary.[5]
"""
)

tproc.newParagraph()

tproc.write(
"""
The enduring popularity of The Lord of the Rings has led to numerous references in popular culture, 
the founding of many societies by fans of Tolkien's works,[6] and the publication of many books about 
Tolkien and his works. The Lord of the Rings has inspired, and continues to inspire, artwork, music, 
films and television, video games, and subsequent literature. Award-winning adaptations of The Lord 
of the Rings have been made for radio, theatre, and film.
"""
)

tproc.stop()

### ### ### ### ### 
import imp, os
path = os.path.abspath("lfn.py")
print path
nm = os.path.basename(path)
mdnm = os.path.splitext(nm)[0]
lfnmodule = imp.load_module("pamparam", open(path), path, ("py", "U", imp.PY_SOURCE))
lfnmodule.foo()

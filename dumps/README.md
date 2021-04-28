# Hexadecimal dumps of Elektronika BRP-2, BRP-3, BRP-4 and BRP-5
Generated automatically from binary dumps, which, in turn, were originally obtained by Sergei Frolov. In particular:
- BRP-2 corresponds to the Elektronika BRP-2 ASTRO unit, as well as to the modified Elektronika BRP-3 unit with the ROM selector resoldered from the "P1" to "P2" position (refer to the schematic diagram)
- BRP-5 corresponds to the modified Elektronika BRP-4 unit with the ROM selector resoldered from the "P2" to "P1" position

Afterwards, for BRP-3, BRP-4 and BRP-5, compared byte-to-byte with dumps generated from those originally manually obtained by apgor. In the case of Elektronika BRP-5 there are four places with different bytes. Will assume that fully automatic dumps (from Sergei Frolov) are more reliable than those partially manual (from apgor).

Note: seems like Elektronika BRP-5 was never officially distributed, manufactured, or even mentioned in the book. Here this name is unofficial and was chosen on the basis of a simple extrapolation of the known names of BRP units, the indices of their ROM chips and the positions of the internal jumpers that select one of the two halves of the ROM chip. Indeed, ROM with index "-0005" and selector in position "P2" gives BRP-2, then -0005 / P1 gives BRP-3, then -0006 / P2 gives BRP-4, so naturally -0006 / P1 should be BRP-5.

The name "BRP-5" was introduced for the first time by the author of this readme file:
- https://www.phantom.sannata.org/viewtopic.php?f=27&t=30810
- http://poligon2.kp4.ru/topic/30810?st=0
- https://web.archive.org/web/20210428010329/http://poligon2.kp4.ru/topic/30810?st=0

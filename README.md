# auto-macro
script to automatically create macros for roll20 for spells in d&amp;d 3.5 using data from dndtools.net

# Usage
Execute extract_macro/extract_macro.exe and copy and paste the link to the spell in dndtools when the prompt asks for it. For example to create a macro of Vampiric Touch you have to input:

```
https://dndtools.net/spells/players-handbook-v35--6/vampiric-touch--2768/
```

Then the script creates macro.txt containing the macro:

```
&{template:DnD35StdRoll} {{spellflag=true}} {{name=@{character_name} }} {{subtags=casts [Vampiric Touch](dndtools.net/spells/players-handbook-v35--6/vampiric-touch--2768/)}}{{School:=Necromancy }}{{Level:= Telflammar Shadowlord 2, Sorcerer 3, Wizard 3, Duskblade 3, Blighter 3, Sha'ir 3, Death Master 3, Dread Necromancer 3, Envy 4, Gluttony 4, }}{{Components:= V, S, }}{{Casting Time:= 1 standard action}}{{Range:= Touch}}{{Target:= Living creature touched}}{{Duration:= Instantaneous/1 hour; see text}}{{Saving Throw:= None}}{{Spell Resistance:= Yes}}{{notes=

You must succeed on a melee touch attack.Your touch deals 1d6 points of damage per two caster levels (maximum 10d6).You gain temporary hit points equal to the damage you deal.However, you can't gain more than the subject's current hitpoints +10, which is enough to kill the subject.The temporary hit points disappear 1 hour later.

}}
```

The macro displays all the info of the spell. With little work you can then get something like this:

```
&{template:DnD35StdRoll} {{spellflag=true}} {{name=@{character_name} }} {{subtags=casts [Vampiric Touch](dndtools.net/spells/players-handbook-v35--6/vampiric-touch--2768/)}}{{School:=Necromancy }}{{Level:= Telflammar Shadowlord 2, Sorcerer 3, Wizard 3, Duskblade 3, Blighter 3, Sha'ir 3, Death Master 3, Dread Necromancer 3, Envy 4, Gluttony 4, }}{{Components:= V, S, }}{{Casting Time:= 1 standard action}}{{Range:= Touch}}{{Target:= Living creature touched}}{{Duration:= Instantaneous/1 hour; see text}}{{Saving Throw:= None}}{{Spell Resistance:= Yes ([[1d20+@{casterlevel}+@{spellpen}]] vs SR)}}{{checkroll= @{character_name} hits Touch AC [[1d20 + @{cha-mod} + @{casterlevel}]] and inflicts [[[[{floor(@{casterlevel}/2), 10}dh1]]d6]] points of damage and gains the same amount of hit points.}}{{notes=

You must succeed on a melee touch attack.Your touch deals 1d6 points of damage per two caster levels (maximum 10d6).You gain temporary hit points equal to the damage you deal.However, you can't gain more than the subject's current hitpoints +10, which is enough to kill the subject.The temporary hit points disappear 1 hour later.

}}
```

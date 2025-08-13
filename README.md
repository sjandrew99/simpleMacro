# simpleMacro

copy-paste macros, nothing fancy. parse a file like this:
SIMPLE_MACRO_DEFS
MACRO0="return 0";
MACRO1="printf(\"hello world\");
printf(\"stuff\n\")";
# a comment
END_SIMPLE_MACRO_DEFS
int main()
{
  $(MACRO1)
  $(MACRO0)
}

rules:
- if SIMPLE_MACRO_DEFS is not the first line of the file, parsing ceases and the output is an exact copy of the input
- macro defs are MACRONAME="TEXT";
    - the surrounding ""; are required. if you need a " in your macro,
      escape it with a backslash (\)
    - no spaces are allowed except inside the "";
- insert a macro with $(MACRONAME). it will be replaced with the macro definition
- comments are allowed in the macro definition section. the first character of the line must be a #
- blank lines are allowed in the macro definition section
- anything else in the macro definition section is an error
- macros may be redefined, although I recommend not doing this
- macro names may contain letters, numbers, and/or underscores

I use .smc (SimpleMaCro) as the extension for a file containing macros but it's not required 

# Usage:
./simpleMacro.py file.c.smc > file.c
./simpleMacro.py --input file.c.smc --output file.c
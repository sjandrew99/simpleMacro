SIMPLE_MACRO_DEFS
MACRO0="return 0;";
MACRO1="int x
=3;";
MACRO2="printf(\"hello world\");
printf(\"stuff\n\");";

# a comment
END_SIMPLE_MACRO_DEFS
#include <stdio.h>
int main()
{
  
  $(MACRO1)
  $(MACRO2)
  $(MACRO0)
}

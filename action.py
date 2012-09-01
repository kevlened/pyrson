#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Owner
#
# Created:     23/08/2012
# Copyright:   (c) Owner 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from dragonfly import (Grammar, AppContext, MappingRule, CompoundRule, Dictation,
                      Choice, Key, Text, Mimic)
from dragonfly.engines.engine import get_engine

engine = get_engine()

class dragonfly_action():
    def load(self, actionfile):
        pass

    def act_on(self, text):
        Mimic("hello")
        return True, " "


#---------------------------------------------------------------------------
# Create this module's grammar and the context under which it'll be active.

grammar = Grammar("notepad_example")


#---------------------------------------------------------------------------
# Create a mapping rule which maps things you can say to actions.
#
# Note the relationship between the *mapping* and *extras* keyword
#  arguments.  The extras is a list of Dragonfly elements which are
#  available to be used in the specs of the mapping.  In this example
#  the Dictation("text")* extra makes it possible to use "<text>"
#  within a mapping spec and "%(text)s" within the associated action.

example_rule = MappingRule(
    name="example",    # The name of the rule.
    mapping={          # The mapping dict: spec -> action.
             #"hello":            Key("c-s"),
             "hello": Text("hi there"),
            },
    )

# Add the action rule to the grammar instance.
grammar.add_rule(example_rule)


#---------------------------------------------------------------------------
# Load the grammar instance and define how to unload it.

grammar.load()
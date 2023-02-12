If the package is too big, you can separate it into several
subpackages, the technique is called package namespaces.

For example, we had this package:
* critters
  * bear.py
  * flamingo.py

It gets too big, so we separate it by location:
* north
  * critters
    * bear.py
* south
  * critters
    * flamingo.py

Then you can add north and south packages to interpreter's packages path (`sys.path.insert()`)
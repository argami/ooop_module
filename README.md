OOOP Module:
--------------------

This is a module to be able to use the OOOP wrapper in a openerp module instead of
the ORM.


*** Advantages ***

1. Less code in the functions
2. Easy to read 
3. You can test the code outside of the openerp


How to install?
---------------------------

1. Install the [OOOP](http://github.com/lasarux/ooop)
2. Clone the repository on your openerp addons folder
3. Update you addons list in your openerp
4. Install the module

How to use?
--------------------
I'm working on some general examples and some examples with unit testing.

but the general idea its this

<pre><code>
def test(self, cr, uid, ids, context=None):
	#here its the magic you can get the ooop
	o = self.pool.get('impulzia.ooop').get(self, cr, uid, ids, context) 
	#start the fun
	x = o.ResPartner.all()
	for i in x:
    	print i.name <http://i.name> <http://i.name>
</code></pre>

How to use OOOP?
--------------------

Just follow the examples in: [OOOP](http://github.com/lasarux/ooop)

Contacting us:
--------------------

Post Issues on github: [GITHUB Issues](http://github.com/argami/ooop_module/issues)
Discussion group:  [openerp-ooop](http://groups.google.es/group/openerp-ooop?hl=en&pli=1)



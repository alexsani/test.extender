from Products.Archetypes.public import StringField, StringWidget
from archetypes.schemaextender.field import ExtensionField

from archetypes.schemaextender.interfaces import ISchemaExtender, IBrowserLayerAwareExtender, IOrderableSchemaExtender, ISchemaModifier
from test.extender.interfaces import ITestExtender

from zope.component import adapts
from zope.interface import implements

from Products.ATContentTypes.content.newsitem import ATNewsItem
from Products.ATContentTypes.interfaces import IATNewsItem

import logging
logger = logging.getLogger('test.extender')


class _ExtensionStringField(ExtensionField, StringField):pass

class ATNewsItemExtender(object):
    """ Extend ATNewsItem
    """
    
    adapts(IATNewsItem)
    implements(ISchemaExtender, IBrowserLayerAwareExtender, IOrderableSchemaExtender, ISchemaModifier)
    layer = ITestExtender
    
    #Add string Field
    fields = [
        _ExtensionStringField(
        name='NuovoCampo',
        widget=StringWidget(
            label='NuovoCampo',
            ),
        required=False,
        ),
    ]
    
    def __init__(self, context):
        self.context = context
        
    def getFields(self):
        return self.fields
        
        
    #Fields reorder
    #Metto il nuovo campo dopo la descrizione
    def getOrder(self, order):
    
        # prendo l'ordine di defaulr
        ci = order['default']

        # prendo l'indice del mio nuovo campo
        aol = ci.index('NuovoCampo')

        # lo metto in cima
        ci.remove('NuovoCampo')
        ci.insert(0, 'NuovoCampo')

        return order
        
    #Fields fiddle     
    def fiddle(object, schema):
        #imposto effectiveDate come obbligatorio
        schema['effectiveDate'].required = True
        return schema
        
        

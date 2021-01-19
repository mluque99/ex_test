import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'ex_test.settings')
import django
django.setup()
from aplicacion.models import Paciente, Medico, Receta


def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.
    add_medico(1,'medico1')
    add_medico(2,'medico2')
    add_medico(3,'medico3')
    add_medico(4,'medico4')
    
    add_paciente(1,'paciente1')
    add_paciente(2,'paciente2')
    add_paciente(3,'paciente3')
    
    add_receta(1,1,1)
    add_receta(2,2,1)
    add_receta(3,1,2)
    add_receta(4,2,2)
    add_receta(5,3,2)

    # Print out the categories we have added.
    print("medicos:")
    for c in Medico.objects.all():
        print('- {0}'.format(str(c)))
    print("pacientes:")
    for c in Paciente.objects.all():
        print('- {0}'.format(str(c)))
    print("recetas:")
    for c in Receta.objects.all():
        print('- {0}'.format(str(c)))


def add_medico(idd,nombre):
    p = Medico.objects.get_or_create(id=idd)[0]
    p.nombreM = nombre
    p.save()
    return p
    
def add_paciente(idd,nombre):
    p = Paciente.objects.get_or_create(id=idd)[0]
    p.nombreP = nombre
    p.save()
    return p

def add_receta(idd,idm,idp):
    p = Receta.objects.get_or_create(id=idd,medico=Medico.objects.get(id=idm),paciente=Paciente.objects.get(id=idp))[0]
    p.save()
    return p

# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()

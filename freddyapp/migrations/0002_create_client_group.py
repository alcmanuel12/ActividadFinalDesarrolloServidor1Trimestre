from django.db import migrations

def create_client_group(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    
    client_group, created = Group.objects.get_or_create(name='Client')
    
    if created:
        animatronic_ct = ContentType.objects.get(app_label='freddyapp', model='animatronic')
        view_permission = Permission.objects.get(
            codename='view_animatronic',
            content_type=animatronic_ct
        )
        client_group.permissions.add(view_permission)

class Migration(migrations.Migration):

    dependencies = [
        ('freddyapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_client_group),
    ]

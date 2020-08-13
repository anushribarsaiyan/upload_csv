from django.shortcuts import render
import io, csv
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import permission_required


# Create your views here.
@permission_required('admin.can_add_log_entry')
def contract_upload(request):
    prompt = {
        'order': 'Order of the csv should  be first_name last_name.email,ip_address,message'
    }
    if request.method == 'GET':
        return render(request, 'upload.html', prompt)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'this not csv file')

    data_set = csv_file.read().decode('UTF-8')
    io.string = io.StringIO(data_set)
    next(io.string)
    for column in csv.reader(io.string, delimiter=',', quotechar="|"):
        _, created = Contract.objects.update_or_create(
            first_name=column[0],
            last_name=column[1],
            email=column[2],
            id_address=column[3],
            message=column[4]
        )

    context = {}
    return render(request, 'upload.html', context)

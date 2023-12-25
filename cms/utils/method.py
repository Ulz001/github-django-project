from cms.serializers.MaterialSerializer import MaterialSerializer, Material


def handling_data(data):
    result = []
    one_data_dict = {}
    for item in data:
        item = dict(item)
        item["material"] = get_material_name(item["material"])

        one_data_dict['name'] = item['material']
        one_data_dict['value'] = item['num']
        result.append(one_data_dict)
        one_data_dict = {}

    return result


def get_material_name(material_id):
    material_name = MaterialSerializer(instance=Material.objects.get(pk=material_id), many=False).data['name']
    return material_name

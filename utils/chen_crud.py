from django.shortcuts import get_object_or_404
from ninja import Schema

class ImportSchema(Schema):
    path: str

# 新增，传入data数据以及model然后添加完成
def create(request, data, model):
    if not isinstance(data, dict):
        data = data.dict()
    query_set = model.objects.create(**data)
    return query_set

# bulk新增，data是{}数组，也就是数组新增
def batch_create(request, data, model):
    data_list = []
    for item in data:
        if not isinstance(item, dict):
            item = item.dict()
    #bulk_create创建，传入是数组，
        data_list.append(model(**item))
    query_set = model.objects.bulk_create(data_list)
    return query_set

# 单个删除
def delete(id, model):
    instance = get_object_or_404(model, id=id)
    instance.delete()
    pass

# 多个删除
def multi_delete(ids,model):
    for item in ids:
        instance = get_object_or_404(model, id=item) # 相当于是model.filter(id=item)
        instance.delete()
    pass

# 更新，data为dict
def update(request, id, data, model):
    dict_data = data.dict()
    ## get_object_or_404如果找到则进行下一步处理，未找到返回404
    instance = get_object_or_404(model, id=id)
    for attr, value in dict_data.items():
        setattr(instance, attr, value)
    instance.save()
    return instance

# 查询
def retrieve(request,model,chenfilters):
    if chenfilters is not None:
        # 将filters空字符串转换为None
        for attr, value in chenfilters.__dict__.items():
            if getattr(chenfilters, attr) == '':
                setattr(chenfilters, attr, None)
        query_set = model.objects.filter(**chenfilters.dict(exclude_none=True))
    else:
        query_set = model.objects.all()
    return query_set


from haystack import indexes
from hos.models import Doctor, Office


# 类名必须为模型名+Index，比如模型Product,则索引类为ProductIndex
class DoctorIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    # 设置模型
    def get_model(self):
        return Doctor

    # 设置查询范围
    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class OfficeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    # 设置模型
    def get_model(self):
        return Office

    # 设置查询范围
    def index_queryset(self, using=None):
        return self.get_model().objects.all()

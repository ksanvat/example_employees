from umongo import MotorAsyncIOInstance


class Instance(MotorAsyncIOInstance):
    def deinit(self):
        self._db = None

    async def ensure_all_indexes(self):
        for doc in self._doc_lookup.values():
            await doc.ensure_indexes()

        for doc in self._embedded_lookup.values():
            await doc.ensure_indexes()

    def register(self, template, as_attribute=True):
        return super().register(template, as_attribute)


instance = Instance()


async def init_instance(db):
    instance.init(db)
    await instance.ensure_all_indexes()


async def deinit_instance():
    instance.deinit()

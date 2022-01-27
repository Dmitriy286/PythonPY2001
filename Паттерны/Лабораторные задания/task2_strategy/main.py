from typing import Iterable

from linked_list import LinkedList
from drivers import IStructureDriver
from factory_method import SimpleFileFactoryMethod, JsonFileDriverFactoryMethod


class LinkedListWithDriver(LinkedList):
    def __init__(self, data: Iterable = None, driver: IStructureDriver = None):
        super().__init__(data)
        self.driver = driver

    @property
    def driver(self) -> IStructureDriver:
        return self._driver

    @driver.setter
    def driver(self, driver) -> None:
        # if not isinstance(driver, IStructureDriver):
        #     raise TypeError()
        self._driver = driver
    # TODO свойство для driver (getter + setter)

    def read(self):
        """ С помощью драйвера считать данные и поместить их в LinkedList. """
        data_from_driver = self.driver.read()

        for value in data_from_driver:
            self.append(value)

    def write(self):
        """ С помощью драйвера записать данные из LinkedList. """
        self.driver.write(self)
        self.driver.write(data=self)


if __name__ == '__main__':
    ll = LinkedListWithDriver()
    driver = SimpleFileFactoryMethod.get_driver()  # TODO инициализировать SimpleFileDriver
    ll.driver = driver
    ll.read()
    print(ll)

    new_driver = JsonFileDriverFactoryMethod.get_driver()
    ll.driver = new_driver  # TODO инициализировать JsonFileDriver
    ll.write()

#fixme что не так?
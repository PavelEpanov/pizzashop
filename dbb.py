import pickle
import shelve

object = SomeClass()
file = open(filenmae, "wb") # Созать новый файл
pickle.dump(object, file)  # Сохранить объект в файле

file = open(filename, "rb")
object = file.load(file) # Извлечь в более позднее время

object2 = SomeClass2()
dbase = shelve.open(filename)
dbase["key"] = object2 # Сохрнаить под ключом

dbase = shelve.open(filenmae)
object2 = dbase["key"] # Извлечь объект в позднее время 
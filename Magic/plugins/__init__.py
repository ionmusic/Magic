from config import LOAD, NOLOAD

def __list_all_modules():
    from os.path import dirname, basename, isfile
    import glob

    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [basename(f)[:-3] for f in mod_paths if isfile(f)
                   and f.endswith(".py")
                   and not f.endswith('__init__.py')]

    if LOAD or NOLOAD:
        to_load = LOAD
        if to_load:
            if not all(any(mod == module_name for module_name in all_modules) for mod in to_load):
                print("Tidak dapat mengimport plugis")
                quit(1)

        else:
            to_load = all_modules

        if NOLOAD:
            print("Plugins tidak terpasang{}".format(NOLOAD))
            return [item for item in to_load if item not in NOLOAD]

        return to_load

    return all_modules


ALL_MODULES = sorted(__list_all_modules())
print("Plugins User Terinstall : %s", str(ALL_MODULES))
__all__ = ALL_MODULES + ["ALL_MODULES"]

from src.backend2.my_filter import MyFilter
from src.backend2.filter_reader import FilterReader
from src.backend2.filter_writer import FilterWriter
from src.backend2.filter_space import FilterSpace


def begin():
    source_path = ".\\resources\\csv\\mATI_sample.csv"
    target_path = ".\\resources\\csv\\ale_speaker.csv"
    save_path = ".\\resources\\csv\\mati_y_ale.csv"

    filter_reader = FilterReader()
    if filter_reader.open_file(source_path):
        source_filter_collection = filter_reader.get_filters()
    else:
        print("ERROR: Could not open source file")
        return

    my_source_filters = []
    for filter_coefficients in source_filter_collection:
        new_filter = MyFilter(filter_coefficients)
        my_source_filters.append(new_filter)

    filter_space = FilterSpace()
    filter_space.add_filters(my_source_filters)
    filter_space.create_tree_from_filters()

    if filter_reader.open_file(target_path):
        target_filter_collection = filter_reader.get_filters()
    else:
        print("ERROR: Could not open target file")
        return

    my_target_filters = []
    for i,filter_coefficients in enumerate(target_filter_collection):
        new_filter = MyFilter(filter_coefficients)
        my_target_filters.append(new_filter)
        if i%100==0:
            print("Done: {}".format(i))

    my_results = []
    for i,target_filter in enumerate(my_target_filters):
        my_results.append(filter_space.get_closest_filter(target_filter))
        if i%100==0:
            print("Done: {}".format(i))

    ready_for_print = []
    for i,result in enumerate(my_results):
        ready_for_print.append(result.get_coefficients())
        if i%100==0:
            print("Done: {}".format(i))

    filter_writer = FilterWriter()
    if filter_writer.save_file(save_path,ready_for_print):
        print("MAJOR SUCCESS!!!")
    else:
        print("a minor inconvenience")


if __name__ == '__main__':
    begin()

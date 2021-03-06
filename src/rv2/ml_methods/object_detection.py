from object_detection.utils import visualization_utils as vis_util

from rv2.core.ml_method import MLMethod
from rv2.evaluations.object_detection_evaluation import (
    ObjectDetectionEvaluation)
from rv2.core.box import Box
from rv2.utils.misc import save_img


def save_debug_image(im, annotations, label_map, output_path):
    npboxes = annotations.get_npboxes()
    class_ids = annotations.get_classes()
    scores = annotations.get_scores()
    if scores is None:
        scores = [1.0] * len(annotations)

    vis_util.visualize_boxes_and_labels_on_image_array(
        im, npboxes, class_ids, scores,
        label_map.get_category_index(), use_normalized_coordinates=True,
        line_thickness=2, max_boxes_to_draw=None)
    save_img(im, output_path)


def make_pos_windows(annotation_source, width, height, chip_size):
    pos_windows = []
    for box in annotation_source.get_all_annotations().get_boxes():
        window = box.make_random_square_container(
            width, height, chip_size)
        pos_windows.append(window)

    return pos_windows


def make_neg_windows(annotation_source, image_extent, chip_size, nb_windows,
                     max_attempts):
    neg_windows = []
    for _ in range(max_attempts):
        window = image_extent.make_random_square(chip_size)
        annotations = annotation_source.get_annotations(
            window, ioa_thresh=0.2)
        if len(annotations) == 0:
            neg_windows.append(window)

        if len(neg_windows) == nb_windows:
            break

    return neg_windows


class ObjectDetection(MLMethod):
    def get_train_windows(self, image_extent, annotation_source, options):
        # Make positive windows which contain annotations.
        pos_windows = make_pos_windows(
            annotation_source, image_extent.get_width(),
            image_extent.get_height(), options.chip_size)

        # Make negative windows which do not contain annotations.
        # Generate randow windows and save the ones that don't contain
        # any annotations. It may take many attempts to generate a single
        # negative window, and could get into an infinite loop in some cases,
        # so we cap the number of attempts.
        nb_neg_windows = \
            int(options.object_detection_options.neg_ratio * len(pos_windows))
        max_attempts = 10 * nb_neg_windows
        neg_windows = make_neg_windows(
            annotation_source, image_extent, options.chip_size, nb_neg_windows,
            max_attempts)

        return pos_windows + neg_windows

    def get_train_annotations(self, window, annotation_source, options):
        return annotation_source.get_annotations(
            window, options.object_detection_options.ioa_thresh)

    def get_predict_windows(self, extent, options):
        chip_size = options.chip_size
        stride = chip_size // 2
        height = extent.get_height()
        width = extent.get_width()

        # TODO make this an iterator
        windows = []
        for row_start in range(0, height, stride):
            for col_start in range(0, width, stride):
                windows.append(
                    Box.make_square(row_start, col_start, chip_size))

        return windows

    def get_evaluation(self):
        return ObjectDetectionEvaluation()

from typing import List, Any

from PyQt6.QtWidgets import QLineEdit, QPushButton, QLabel, QComboBox, QCheckBox, QSpacerItem, QSizePolicy


def create_button(text: str, callback: Any):
    """
    Creates a Button component.
    :param text: The text to be displayed on the button.
    :param callback: The method to be called when the button is clicked on.
    :return: A QButton instance.
    """
    button = QPushButton(text)
    button.clicked.connect(callback)

    return button


def create_check_box(text: str,
                     is_checked: bool,
                     state_changed,
                     is_enabled: bool = True,
                     tooltip: str = None,

):
    """
    Creates a Checkbox component
    :param text: Text that describes what this Check Box is for.
    :param is_checked:  True if the checkbox is checked, False otherwise.
    :param state_changed: The method to be called when the check box state changes. (Default = True)
    :param is_enabled: True if the user can interact with the widget, False if not.
    :param tooltip: The text to show when the user hovers over the check box (Default = None)
    :return: A QCheckBox instance
    """
    check_box = QCheckBox()
    check_box.setText(text)
    check_box.setChecked(is_checked)
    check_box.setEnabled(is_enabled)
    check_box.stateChanged.connect(state_changed)

    if tooltip is not None:
        check_box.setToolTip(tooltip)

    return check_box


def create_combo_box(placeholder: str,
                     items: [Any],
                     current_index_changed: Any,
                     current_item_index: int = None,

):
    """
    Creates a Combo Box component
    :param placeholder: The placeholder text for the combo box
    :param items: A List of items the combo box uses.
    :param current_item_index: The item currently selected.
    :param current_index_changed: The method to be called when the current index changes.
    :return: A QComboBox instance.
    """
    combo = QComboBox()
    combo.setPlaceholderText(placeholder)
    combo.addItems(items)
    combo.currentIndexChanged.connect(current_index_changed)

    if current_item_index is not None:
        combo.setCurrentIndex(current_item_index)

    return combo


def create_label(text: str):
    """
    Creates a Label component.
    :param text -- The text to be displayed
    :return: A QLabel instance
    """
    label = QLabel(text)

    return label


def create_line_edit(placeholder: str, callback):
    """
    Creates a Line Edit component.
    :param placeholder: The text to be displayed if the line edit has not been written in
    :param callback: The method to be called when the line edit text is changed.
    :return: A QLineEdit instance.
    """
    line_edit = QLineEdit()
    line_edit.setPlaceholderText(placeholder)
    line_edit.textChanged.connect(callback)

    return line_edit


def create_spacer_item(h_policy: QSizePolicy = QSizePolicy.Policy.Expanding,
                       v_policy: QSizePolicy = QSizePolicy.Policy.Fixed,
                       width: int = 20,
                       height: int = 20,
):
    """
    Creates a Spacer Item Component.
    :param h_policy: The Horizontal Policy to be used by the spacer. (Default = Expanding)
    :param v_policy: The Vertical Policy to be used by the spacer. (Default = Fixed)
    :param width: The width of the spacer. (Default = 20)
    :param height: The height of the spacer. (Default = 20)
    :return: A QSpacerItem instance
    """
    return QSpacerItem(width, height, h_policy, v_policy)

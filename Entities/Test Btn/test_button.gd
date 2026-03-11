extends Button
signal input_text_signal(text_itself: StringName)

@export var TextInputBox: TextEdit
var input_text: StringName

func _ready() -> void:
	pressed.connect(receive_data)
	_check_connected_nodes()
	send_data()

func send_data() -> void:
	input_text = TextInputBox.text
	input_text_signal.emit(input_text)
	print(input_text)

func receive_data() -> void:
	input_text = TextInputBox.text
	print(input_text)

## Reports an error if the requered nodes aren't connected
func _check_connected_nodes() -> void:
	if TextInputBox == null:
		printerr("No TextInputBox connected ", str(self)); print_debug()

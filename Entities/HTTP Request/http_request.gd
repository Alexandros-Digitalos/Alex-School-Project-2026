extends HTTPRequest

@export var data: PackedStringArray
@export var url: String

func _ready() -> void:
	# Connects the HTTP Node to a function which porccesses its data
	request_completed.connect(_on_request_completed)
	print(get_downloaded_bytes())

## Outputs the recieved web data
func _on_request_completed(result: int, response_code: int, headers: PackedStringArray, body: PackedByteArray) -> void:
	var response = body.get_string_from_utf8()
	print(response)

## See a list of the IP Interfaces
func see_ip() -> void:
	var addresses: PackedStringArray = IP.get_local_addresses()
	for ip: String in addresses:
		print("Interface IP: ", ip)

import inspect
import os

def ros2_action_decorator(func):
    func_name = func.__name__

    # Inspect function signature
    signature = inspect.signature(func)
    param_types = {k: v.annotation for k, v in signature.parameters.items()}
    return_type = signature.return_annotation

    # Generate .msg and .action files
    msg_dir = "ros2_action_decorator_msgs/msg"
    action_dir = "ros2_action_decorator_msgs/action"
    os.makedirs(msg_dir, exist_ok=True)
    os.makedirs(action_dir, exist_ok=True)

    # Create message files
    input_msg = f"{func_name}Input.msg"
    output_msg = f"{func_name}Output.msg"

    with open(os.path.join(msg_dir, input_msg), "w") as f:
        for name, type_ in param_types.items():
            f.write(f"{type_.__name__} {name}\n")

    with open(os.path.join(msg_dir, output_msg), "w") as f:
        f.write(f"{return_type.__name__} result\n")

    # Create action file
    action_file = os.path.join(action_dir, f"{func_name}.action")
    with open(action_file, "w") as f:
        for name, type_ in param_types.items():
            f.write(f"{type_.__name__} {name}\n")
        f.write("---\n")
        f.write(f"{return_type.__name__} result\n")
        f.write("---\n")
        f.write("float32 progress\n")

    print(f"Generated {input_msg}, {output_msg}, and {func_name}.action")

    return func

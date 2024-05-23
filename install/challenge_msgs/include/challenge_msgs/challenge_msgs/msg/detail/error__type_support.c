// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from challenge_msgs:msg/Error.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "challenge_msgs/msg/detail/error__rosidl_typesupport_introspection_c.h"
#include "challenge_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "challenge_msgs/msg/detail/error__functions.h"
#include "challenge_msgs/msg/detail/error__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void challenge_msgs__msg__Error__rosidl_typesupport_introspection_c__Error_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  challenge_msgs__msg__Error__init(message_memory);
}

void challenge_msgs__msg__Error__rosidl_typesupport_introspection_c__Error_fini_function(void * message_memory)
{
  challenge_msgs__msg__Error__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember challenge_msgs__msg__Error__rosidl_typesupport_introspection_c__Error_message_member_array[2] = {
  {
    "center_error",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(challenge_msgs__msg__Error, center_error),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "points_error",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(challenge_msgs__msg__Error, points_error),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers challenge_msgs__msg__Error__rosidl_typesupport_introspection_c__Error_message_members = {
  "challenge_msgs__msg",  // message namespace
  "Error",  // message name
  2,  // number of fields
  sizeof(challenge_msgs__msg__Error),
  challenge_msgs__msg__Error__rosidl_typesupport_introspection_c__Error_message_member_array,  // message members
  challenge_msgs__msg__Error__rosidl_typesupport_introspection_c__Error_init_function,  // function to initialize message memory (memory has to be allocated)
  challenge_msgs__msg__Error__rosidl_typesupport_introspection_c__Error_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t challenge_msgs__msg__Error__rosidl_typesupport_introspection_c__Error_message_type_support_handle = {
  0,
  &challenge_msgs__msg__Error__rosidl_typesupport_introspection_c__Error_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_challenge_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, challenge_msgs, msg, Error)() {
  if (!challenge_msgs__msg__Error__rosidl_typesupport_introspection_c__Error_message_type_support_handle.typesupport_identifier) {
    challenge_msgs__msg__Error__rosidl_typesupport_introspection_c__Error_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &challenge_msgs__msg__Error__rosidl_typesupport_introspection_c__Error_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

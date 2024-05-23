// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from challenge_msgs:msg/Error.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "challenge_msgs/msg/detail/error__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace challenge_msgs
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void Error_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) challenge_msgs::msg::Error(_init);
}

void Error_fini_function(void * message_memory)
{
  auto typed_message = static_cast<challenge_msgs::msg::Error *>(message_memory);
  typed_message->~Error();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember Error_message_member_array[2] = {
  {
    "center_error",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(challenge_msgs::msg::Error, center_error),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "points_error",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(challenge_msgs::msg::Error, points_error),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers Error_message_members = {
  "challenge_msgs::msg",  // message namespace
  "Error",  // message name
  2,  // number of fields
  sizeof(challenge_msgs::msg::Error),
  Error_message_member_array,  // message members
  Error_init_function,  // function to initialize message memory (memory has to be allocated)
  Error_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t Error_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &Error_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace challenge_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<challenge_msgs::msg::Error>()
{
  return &::challenge_msgs::msg::rosidl_typesupport_introspection_cpp::Error_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, challenge_msgs, msg, Error)() {
  return &::challenge_msgs::msg::rosidl_typesupport_introspection_cpp::Error_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from challenge_msgs:msg/Error.idl
// generated code does not contain a copyright notice

#ifndef CHALLENGE_MSGS__MSG__DETAIL__ERROR__TRAITS_HPP_
#define CHALLENGE_MSGS__MSG__DETAIL__ERROR__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "challenge_msgs/msg/detail/error__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace challenge_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const Error & msg,
  std::ostream & out)
{
  out << "{";
  // member: center_error
  {
    out << "center_error: ";
    rosidl_generator_traits::value_to_yaml(msg.center_error, out);
    out << ", ";
  }

  // member: points_error
  {
    out << "points_error: ";
    rosidl_generator_traits::value_to_yaml(msg.points_error, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Error & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: center_error
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "center_error: ";
    rosidl_generator_traits::value_to_yaml(msg.center_error, out);
    out << "\n";
  }

  // member: points_error
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "points_error: ";
    rosidl_generator_traits::value_to_yaml(msg.points_error, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Error & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace challenge_msgs

namespace rosidl_generator_traits
{

[[deprecated("use challenge_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const challenge_msgs::msg::Error & msg,
  std::ostream & out, size_t indentation = 0)
{
  challenge_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use challenge_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const challenge_msgs::msg::Error & msg)
{
  return challenge_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<challenge_msgs::msg::Error>()
{
  return "challenge_msgs::msg::Error";
}

template<>
inline const char * name<challenge_msgs::msg::Error>()
{
  return "challenge_msgs/msg/Error";
}

template<>
struct has_fixed_size<challenge_msgs::msg::Error>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<challenge_msgs::msg::Error>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<challenge_msgs::msg::Error>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // CHALLENGE_MSGS__MSG__DETAIL__ERROR__TRAITS_HPP_

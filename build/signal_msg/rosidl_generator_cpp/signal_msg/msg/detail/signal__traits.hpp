// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from signal_msg:msg/Signal.idl
// generated code does not contain a copyright notice

#ifndef SIGNAL_MSG__MSG__DETAIL__SIGNAL__TRAITS_HPP_
#define SIGNAL_MSG__MSG__DETAIL__SIGNAL__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "signal_msg/msg/detail/signal__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace signal_msg
{

namespace msg
{

inline void to_flow_style_yaml(
  const Signal & msg,
  std::ostream & out)
{
  out << "{";
  // member: name
  {
    out << "name: ";
    rosidl_generator_traits::value_to_yaml(msg.name, out);
    out << ", ";
  }

  // member: num
  {
    out << "num: ";
    rosidl_generator_traits::value_to_yaml(msg.num, out);
    out << ", ";
  }

  // member: reliability
  {
    out << "reliability: ";
    rosidl_generator_traits::value_to_yaml(msg.reliability, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Signal & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "name: ";
    rosidl_generator_traits::value_to_yaml(msg.name, out);
    out << "\n";
  }

  // member: num
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "num: ";
    rosidl_generator_traits::value_to_yaml(msg.num, out);
    out << "\n";
  }

  // member: reliability
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "reliability: ";
    rosidl_generator_traits::value_to_yaml(msg.reliability, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Signal & msg, bool use_flow_style = false)
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

}  // namespace signal_msg

namespace rosidl_generator_traits
{

[[deprecated("use signal_msg::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const signal_msg::msg::Signal & msg,
  std::ostream & out, size_t indentation = 0)
{
  signal_msg::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use signal_msg::msg::to_yaml() instead")]]
inline std::string to_yaml(const signal_msg::msg::Signal & msg)
{
  return signal_msg::msg::to_yaml(msg);
}

template<>
inline const char * data_type<signal_msg::msg::Signal>()
{
  return "signal_msg::msg::Signal";
}

template<>
inline const char * name<signal_msg::msg::Signal>()
{
  return "signal_msg/msg/Signal";
}

template<>
struct has_fixed_size<signal_msg::msg::Signal>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<signal_msg::msg::Signal>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<signal_msg::msg::Signal>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SIGNAL_MSG__MSG__DETAIL__SIGNAL__TRAITS_HPP_

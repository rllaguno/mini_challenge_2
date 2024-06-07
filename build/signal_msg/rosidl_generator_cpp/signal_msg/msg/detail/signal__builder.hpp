// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from signal_msg:msg/Signal.idl
// generated code does not contain a copyright notice

#ifndef SIGNAL_MSG__MSG__DETAIL__SIGNAL__BUILDER_HPP_
#define SIGNAL_MSG__MSG__DETAIL__SIGNAL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "signal_msg/msg/detail/signal__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace signal_msg
{

namespace msg
{

namespace builder
{

class Init_Signal_reliability
{
public:
  explicit Init_Signal_reliability(::signal_msg::msg::Signal & msg)
  : msg_(msg)
  {}
  ::signal_msg::msg::Signal reliability(::signal_msg::msg::Signal::_reliability_type arg)
  {
    msg_.reliability = std::move(arg);
    return std::move(msg_);
  }

private:
  ::signal_msg::msg::Signal msg_;
};

class Init_Signal_num
{
public:
  explicit Init_Signal_num(::signal_msg::msg::Signal & msg)
  : msg_(msg)
  {}
  Init_Signal_reliability num(::signal_msg::msg::Signal::_num_type arg)
  {
    msg_.num = std::move(arg);
    return Init_Signal_reliability(msg_);
  }

private:
  ::signal_msg::msg::Signal msg_;
};

class Init_Signal_name
{
public:
  Init_Signal_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Signal_num name(::signal_msg::msg::Signal::_name_type arg)
  {
    msg_.name = std::move(arg);
    return Init_Signal_num(msg_);
  }

private:
  ::signal_msg::msg::Signal msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::signal_msg::msg::Signal>()
{
  return signal_msg::msg::builder::Init_Signal_name();
}

}  // namespace signal_msg

#endif  // SIGNAL_MSG__MSG__DETAIL__SIGNAL__BUILDER_HPP_

#include <rclcpp/rclcpp.hpp>
#include <rclcpp_action/rclcpp_action.hpp>
#include "example_action.hpp"

class ExampleActionServer : public rclcpp::Node {
public:
    using ActionType = ExampleAction;

    ExampleActionServer() : Node("example_action_server") {
        action_server_ = rclcpp_action::create_server<ActionType>(
            this,
            "example",
            std::bind(&ExampleActionServer::handle_goal, this, std::placeholders::_1, std::placeholders::_2),
            std::bind(&ExampleActionServer::handle_cancel, this, std::placeholders::_1),
            std::bind(&ExampleActionServer::handle_accepted, this, std::placeholders::_1)
        );
    }

private:
    rclcpp_action::Server<ActionType>::SharedPtr action_server_;

    rclcpp_action::GoalResponse handle_goal(
        const rclcpp_action::GoalUUID & uuid,
        std::shared_ptr<const ActionType::Goal> goal) {
        RCLCPP_INFO(this->get_logger(), "Received goal request");
        return rclcpp_action::GoalResponse::ACCEPT_AND_EXECUTE;
    }

    rclcpp_action::CancelResponse handle_cancel(
        const std::shared_ptr<GoalHandle> goal_handle) {
        RCLCPP_INFO(this->get_logger(), "Received request to cancel goal");
        return rclcpp_action::CancelResponse::ACCEPT;
    }

    void handle_accepted(const std::shared_ptr<GoalHandle> goal_handle) {
        RCLCPP_INFO(this->get_logger(), "Executing goal");
        goal_handle->succeed(std::make_shared<ActionType::Result>());
    }
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<ExampleActionServer>());
    rclcpp::shutdown();
    return 0;
}

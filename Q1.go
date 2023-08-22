package main

import "fmt"

type Ivehicle interface {
	start()
	sound()
}

type vehicle struct {
}

func (c *vehicle) start() {
	fmt.Println("vehicle start")
}

type car struct {
	vehicle
}
func (c *car)sound(){
	fmt.Println("boom~ boom~ boom~")
}

type motor struct {
	vehicle
}
func (m *motor)sound(){
	fmt.Println("booooo~")
}

func NewEmployee(vehicle Ivehicle)(em *employee){
	var employee employee
	employee.vehicle = vehicle
	return &employee
}

type employee struct {
	vehicle Ivehicle
}

func (e *employee) go_to_work() {
	e.vehicle.start()
	e.vehicle.sound()
}

// employee 實例化時要注入 vehicle 且 vehicle 要符合 Ivehicle 介面
// car 跟 motor 本身並沒有實作 Ivehicle 介面的 start 方法
// car 跟 motor 透過繼承 vehicle_class 來繼承了 start 方法
// 並自己實現了sound方法，以符合 Ivehicle 介面

func main() {
	var car car
	employee1 := NewEmployee(&car)
	employee1.go_to_work()

	var motor motor
	employee2 := NewEmployee(&motor)
	employee2.go_to_work()
}
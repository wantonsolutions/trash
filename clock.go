package main

func main() {
	for i:=0;i < 100;i++ {
		fmt.Println(clock(i))
	}
}

func clock(counter int) string {
	seconds := counter % 60
	count /= 60
	minutes := counter % 60
	count /= 60
	hours := counter % 24
	return fmt.Sprintf("%2d:%2d:%2d")
}
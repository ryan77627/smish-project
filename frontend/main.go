package main

import (
	"fmt"
	"html/template"
	"net/http"
	"strconv"

	util "github.com/ryan77627/smish-project/frontend/util"
)

const (
	PORT = 8080
	TPL  = "template/*.html"
)

type Full struct {
	Sidebar  Side
	Network  Net
	Bargraph Bar
}

type Side struct {
	Navs []string
}

type Bar struct {
	Hi string
}

type Net struct {
	Hi string
}

func root(w http.ResponseWriter, r *http.Request) {
	tpl := template.Must(template.ParseGlob(TPL))
	tpl.ExecuteTemplate(w, "preview", nil)
}

func console(w http.ResponseWriter, r *http.Request) {
	tpl := template.Must(template.ParseGlob(TPL))
	full := Full{
		Sidebar: Side{
			Navs: []string{"Home", "Dashboard"},
		},
		Network:  Net{Hi: "asdfsa"},
		Bargraph: Bar{Hi: "asdj"},
	}
	// full := Full.Sidebar
	tpl.ExecuteTemplate(w, "admin-console", full)
}

func preview(w http.ResponseWriter, r *http.Request) {
	tpl := template.Must(template.ParseGlob(TPL))
	tpl.ExecuteTemplate(w, "preview", nil)
}

func main() {
	port := strconv.Itoa(PORT)

	http.HandleFunc("/", root)
	http.HandleFunc("/console", console)
	http.HandleFunc("/preview", preview)

	fmt.Printf("Running on\nhttp://localhost:%s\n", port)

	util.Check(http.ListenAndServe(":"+port, nil))

}

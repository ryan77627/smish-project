package main

import (
	"fmt"
	"net/http"
	"strconv"
	"text/template"
)

const (
	PORT = 8080
	TPL  = "templates/*.html"
)

func console(w http.ResponseWriter, r *http.Request) {
	tpl := template.Must(template.ParseGlob(TPL))
	tpl.ExecuteTemplate(w, "main", nil)
}

func preview(w http.ResponseWriter, r *http.Request) {
	tpl := template.Must(template.ParseGlob(TPL))
	tpl.ExecuteTemplate(w, "main", nil)
}

func sign(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "yes")
}

func root(w http.ResponseWriter, r *http.Request) {
	tpl := template.Must(template.ParseGlob(TPL))
	tpl.ExecuteTemplate(w, "main", nil)
}

func main() {
	port := strconv.Itoa(PORT)

	http.HandleFunc("/", root)
	http.HandleFunc("/console", console)
	http.HandleFunc("/preview", preview)
	http.HandleFunc("/sign", sign)

	fmt.Printf("Running on\nhttp://localhost:%s\n", port)

	util.Check(http.ListenAndServe(":"+port, nil))

}

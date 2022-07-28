package util

import (
	"io/ioutil"
	"net/http"
	"net/url"
)

const (
	site      = "https://theinfoseccorner.com/api/"
	gTree     = "genTree"
	gCampaign = "getCampaigns"
	gcDetails = "getCampaignDetails"
)

func GetOrg(name string) string {
	// url encode so you can just put in string
	s := url.QueryEscape(name)
	endpoint := site + gTree + "?user=" + s

	// fmt.Printf(endpoint)
	resp, err := http.Get(endpoint)
	Check(err)

	body, err := ioutil.ReadAll(resp.Body)
	Check(err)

	return string(body)
}

func GetCampaigns() string {
	endpoint := site + gCampaign
	// fmt.Printf(endpoint)
	resp, err := http.Get(endpoint)
	Check(err)

	body, err := ioutil.ReadAll(resp.Body)
	Check(err)

	return string(body)
}

func GetCampaignDetails(campaign_id string) string {
	s := url.QueryEscape(campaign_id)
	endpoint := site + gcDetails + "?campaign_id=" + s

	resp, err := http.Get(endpoint)
	Check(err)

	body, err := ioutil.ReadAll(resp.Body)
	Check(err)

	return string(body)
}

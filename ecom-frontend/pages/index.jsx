import Head from 'next/head'
import Image from 'next/image'
import Home from 'components/Home/Home'
import HomeLayout from '../components/layouts/HomeLayout'


export default function HomePage() {
  return (
    <Home />
  )
}


HomePage.getLayout = function getLayout(page) {
  return (
    <HomeLayout>
      {page}
    </HomeLayout>
  )
}
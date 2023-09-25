import Head from 'next/head'
import Image from 'next/image'
import Signin from 'components/Signin/Signin'
import NormalLayout from 'components/layouts/NormalLayout'


export default function SigninPage() {
  return (
    <>
    <Head>
        <title>Sign in</title>
        <meta name="description" content="Sign in" />
    </Head>
    <Signin />
    </>
    
  )
}


SigninPage.getLayout = function getLayout(page) {
  return (
    <NormalLayout>
      {page}
    </NormalLayout>
  )
}